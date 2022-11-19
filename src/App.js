import React from 'react';
import { Route, Routes } from 'react-router';
import { Link } from 'react-router-dom';
import Home from './pages/Home';

class App extends React.Component {
  render() {
    return (
      <div className="App" >
        <div>
          <nav>
            <ul id="navigation">
              <li>
                <Link to="/home">Home</Link>
              </li>
              <li>
                <Link to="/about">About</Link>
              </li>
              <li>
                <Link to="/contact">Contact</Link>
              </li>
            </ul>
          </nav>
        </div>
        <Routes>
          <Route exact path="/home" element={<Home />} />
        </Routes>
      </div>
    );
  }
}
export default App;
