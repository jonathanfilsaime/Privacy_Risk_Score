import React, {Component} from 'react';
import {connect} from 'react-redux';
import { Link } from "react-router-dom";
import getScoreAction from './actions';

import Recommendations from '../Recommendations';

import './styles.css';

class Score extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: true
    }
  }
  componentDidMount() {
    setTimeout( () => {
        this.props.getScoreAction();
        setTimeout( () => {
            this.setState({loading: false})
          }
          , 2000);
      }
      , 2000);
  }

  render() {
    if(this.state.loading) {
      return (<h1 className="Score-loading">Calculating score...</h1>);
    }

    return (
      <div className="Score">
        <div className="Score-score-section">
          <Link to="/" className="Score-retake">Retake</Link>
          <h1 className="Score-header">Privacy Risk Score</h1>

          <div className="Score-stats">
            <div className="Score-secondary-stats">
              avg: {this.props.score.score[0].average}
            </div>
            <div className="Score-score">
              {this.props.score.score[0].score}%
            </div>
            <div className="Score-secondary-stats">
              total: {this.props.score.score[0].total}
            </div>
          </div>

          <Link to="dashboard" className="Score-link">
            <span>Admin dashboard</span>
          </Link>
        </div>
        <Recommendations rec={this.props.score.rec}/>
      </div>
    );
  }
}

const mapStateToProps = function(state) {
  return {
    score: state.score
  }
}

export default connect(mapStateToProps, {getScoreAction})(Score);

/*
<div className="Score-share">
  <img src="http://www.kaceni-teplice.cz/images/fb_icon_325x325.png" />
  <img src="https://selfpublishingadvice.org/wp-content/uploads/2013/10/twitter-200x200.png" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png" />
</div>
*/
