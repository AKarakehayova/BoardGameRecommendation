import React from 'react'
import ReactDOM from 'react-dom'
import {Router, Route, Switch} from 'react-router-dom'


// components and pages
import App from './App.jsx'

ReactDOM.render((
  <Router>
    <Switch>
      <Route exact path='/' component={App} />

    </Switch>
  </Router>
),
document.getElementById('root')
)
