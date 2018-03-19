import React, {Component} from 'react';
import banner from '../../images/banner.jpg';

import './styles.css';

class Header extends Component {
  render() {
    return (
      <div className="Header" >
        <img src={banner} className="Header-banner" />
      </div>
    );
  }
}

export default Header;
