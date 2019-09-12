import React from 'react';
import { withAuth } from '@okta/okta-react';

import StickyNote from '../StickyNote';
//
// const home = (props) => {
//   return (
//     <div>Home... Hello!</div>
//   )
// };

class Home extends React.Component {
  render () {
    return(
    <StickyNote />
    )
  }
}

export default Home;

// export default withAuth(Home);
