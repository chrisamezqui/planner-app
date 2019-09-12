import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const styles = themes => ({
  card: {
    width: 260,
    minHeight: 350,
  },
  title: {
    fontSize: 32,
  },
  body: {
    fontSize: 14,
  },
});

class StickyNote extends React.Component {

  render() {
    const { classes } = this.props;
    return (
      <Card className={classes.card}>
        <CardContent>
          <Typography className={classes.title} align="center" comoponent="h1" gutterBottom>
            Sample Title
          </Typography>
          <Typography className={classes.body} component="p" gutterBottom>
            This is a note. Hello.
          </Typography>
        </CardContent>
      </Card>
    );
  }
}

export default withStyles(styles)(StickyNote);
