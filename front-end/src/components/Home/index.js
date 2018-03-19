import React, {Component} from 'react';
import { Link } from "react-router-dom";

import family from '../../images/family.png';
import './styles.css';

class Home extends Component {
  render() {
    return (
      <div className="Home" >
        <h1 className="Home-header">Protect those you love</h1>
        <div className="buttons-coll">
          <Link to="/quiz">
            <button className="custom-btn btn-5"><span>Take Quiz</span></button>
          </Link>
          <Link to="/score" className="Home-already">
            <span>Already taken the quiz?</span>
          </Link>
        </div>
      </div>
    );
  }
}

export default Home;
