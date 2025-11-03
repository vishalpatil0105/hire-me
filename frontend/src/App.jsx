import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Auth from './pages/Auth';
import Home from './pages/Home';
import Admin from './pages/Admin';
import Header from './components/Header';

const App = () => {
  return (
    <Router>
      <Header />
      <Switch>
        <Route path="/auth" component={Auth} />
        <Route path="/admin" component={Admin} />
        <Route path="/home" component={Home} />
        <Route path="/" exact component={Auth} />
      </Switch>
    </Router>
  );
};

export default App;