import React, { Component } from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom'
import { Security, ImplicitCallback, SecureRoute } from '@okta/okta-react';

import Login from '../Login'
import Home from '../Home'

class Main extends Component {
 render() {
   const clientId = "0oa18ljdanvKYSeQ8357";
   const oktaDomain = "https://dev-662087.okta.com";
   return (
     <Router>
       <Security
         issuer={oktaDomain}
         client_id={clientId}
         redirect_uri={'http://localhost:3000/implicit/callback'}
         scope={['openid', 'profile', 'email']}>

         <Switch>
           <Route exact path="/" component={Login} />
           <Route path="/implicit/callback" component={ImplicitCallback} />
           <SecureRoute path="/home" component={Home} />
         </Switch>
       </Security>
     </Router>
   );
 }
}

export default Main;
