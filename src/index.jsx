import React from 'react'
import ReactDOM from 'react-dom'
import {Router, Route, Switch} from 'react-router-dom'
import "react-table/react-table.css";
import history from './history'

// components and pages
import App from './App.jsx'

ReactDOM.render((
  <Router history={history}>
    <Switch>
      <Route exact path='/' component={App} />

    </Switch>
  </Router>
),
document.getElementById('root')
)
