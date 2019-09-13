import React from 'react';
import { withAuth } from '@okta/okta-react';

import StickyNote from '../StickyNote';

class Home extends React.Component {
  render () {
    return(
    <StickyNote />
    )
  }
}

export default Home;

// export default withAuth(Home);
