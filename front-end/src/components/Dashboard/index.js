import React, {Component} from 'react';
import {connect} from 'react-redux';
import {Link} from 'react-router-dom';
import getDashboardAction from './actions';

import NumPeople from '../NumPeople';
import './styles.css';

class Dashboard extends Component {
  componentDidMount() {
    this.props.getDashboardAction();
  }

  render() {
    if(this.props.dashboard.length === 0){
      return null;
    }

    return (
      <div>
    <Link to="/score" > back </Link>
        <div className="Dashboard">
          <NumPeople
            caption={'People took this quiz'}
            data={this.props.dashboard[0]['visits']}
          />
          <NumPeople
            caption={'Got a perfect score'}
            data={`${this.props.dashboard[0]['credit monitoring']}%`}
          />
          <NumPeople
            caption={'Average social media score'}
            data={`${this.props.dashboard[0]['social media']}%`}
          />
          <NumPeople
            caption={'Average credit monitoring score'}
            data={`${this.props.dashboard[0]['credit monitoring']}%`}
          />
          <NumPeople
            caption={'Average authentication score'}
            data={`${this.props.dashboard[0]['authentication']}%`}
          />
          <NumPeople
            caption={'Average devices score'}
            data={`${this.props.dashboard[0]['devices']}%`}
          />
        </div>
      </div>
    );
  }
}

const mapStateToProps = function(state) {
  return {
    dashboard: state.dashboard
  }
}

export default connect(mapStateToProps, {getDashboardAction})(Dashboard);
