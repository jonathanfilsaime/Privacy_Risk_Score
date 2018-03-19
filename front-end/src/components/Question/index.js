import React, {Component} from 'react';
import { Field, reduxForm } from 'redux-form';
import {connect} from 'react-redux';
import validate from './validate';

import './styles.css';

class Question extends Component {
  constructor(props) {
    super(props);

    this.renderAnswers = this.renderAnswers.bind(this);
  }

  renderAnswers() {
    return  this.props.answers.map((answer, index) => {
      return (
        <div key={answer.answer}>
          <Field
              id={index}
              name={answer.id.toString()}
              component="input"
              type="radio"
              value={answer.answer}
           />
          <label for={index} className="Question-label">{answer.answer}</label>
        </div>
      )
    });
  }

  render() {
    let {index, questions, pristine} = this.props;

    let nextButton = (index !== questions.length - 1) ? 'Next Question' : 'Submit';

    return (
      <form className="Question" onSubmit={this.props.handleSubmit(this.props.onNext)}>
        <h2 className="Question-header">{this.props.question}</h2>
        <div className="Question-questions">
          <div className="Question-answers">
            {this.renderAnswers()}
          </div>
          <div className="Question-buttons">
              <button
                className="button"
                disabled={!index}
                onClick={this.props.onPrev}
              >
                Prev Question
              </button>
            {
              <button
                className="button"
                disabled={!this.props.valid}
                type="submit"
              >
                {nextButton}
              </button>
            }
          </div>
        </div>
      </form>
    );
  }
}

export default reduxForm({
  form: 'wizard',
  destroyOnUnmount: false,
  forceUnregisterOnUnmount: true,
  validate
})(Question);
