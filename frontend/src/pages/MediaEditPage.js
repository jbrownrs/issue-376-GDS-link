import React, { Component } from 'react';

import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';

import Page from '../containers/Page';
import ItemMetadataForm from "../components/ItemMetadataForm";
import {mediaGet, mediaPatch} from "../api";
import { setMessageForNextPageLoad } from "../containers/Snackbar";
import IfOwnsChannel from "../containers/IfOwnsChannel";

/**
 * A page which allows the user to edit a media item's metadata.
 */
class MediaEditPage extends Component {
  constructor(props) {
    super(props);

    this.state = {
      // An error object as returned by the API or the empty object if there are no errors.
      errors: {},
      // The media item being edited by the ItemMetadataForm.
      item: { id: '' },
    };
  }

  /** Gets the media item's id. */
  getItemId = () => this.props.match.params.pk;

  /**
   * Retrieve the item.
   */
  componentWillMount() {
    mediaGet(this.getItemId()).then(item => this.setState({ item }));
  }

  /**
   * Save the edited item.
   */
  save() {
    mediaPatch(this.state.item)
      .then(() => {
        setMessageForNextPageLoad('The media item has been updated.');
        window.location = '/media/' + this.getItemId()
      })
      .catch(({ body }) => this.setState({ errors: body })
    );
  }

  render() {
    const { classes } = this.props;
    const { item, errors } = this.state;
    return (
      <Page>
        <section className={classes.section}>
          <IfOwnsChannel channel={item && item.channel}>
            <Grid container justify='center'>
              <Grid item xs={12} sm={10} md={8} lg={6}>
                <ItemMetadataForm
                  item={item}
                  errors={errors}
                  onChange={patch => this.setState({item: {...item, ...patch}})}
                />
                <div className={ classes.buttonSet }>
                  <Button variant='outlined' href={ '/media/' + this.getItemId() } >
                    Cancel
                  </Button>
                  <Button color='secondary' variant='contained' onClick={ () => this.save() } >
                    Save
                  </Button>
                </div>
              </Grid>
            </Grid>
          </IfOwnsChannel>
          <IfOwnsChannel channel={item && item.channel} hide>
            <Typography variant="headline" component="div">
              You cannot edit this media item.
            </Typography>
          </IfOwnsChannel>
        </section>
      </Page>
    );
  }
}

const styles = theme => ({
  buttonSet: {
    '& button': {
      marginLeft: theme.spacing.unit,
    },
    marginTop: theme.spacing.unit,
    textAlign: 'right',
  },
  section: {
    marginTop: theme.spacing.unit,
  },
});

export default withStyles(styles)(MediaEditPage);
