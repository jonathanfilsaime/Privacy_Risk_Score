import React, {Component} from 'react';
import {connect} from 'react-redux';
import { Field, reduxForm } from 'redux-form'
import {getSurveyAction, postSurveyAnswers} from './actions';

import './styles.css'

import Question from '../Question/';

class Quiz extends Component {
  constructor(props) {
    super(props);

    this.state = {
      index: 0
    }
    this.renderQuestions = this.renderQuestions.bind(this);
    this.nextQuestion = this.nextQuestion.bind(this);
    this.prevQuestion = this.prevQuestion.bind(this);
    this.submit = this.submit.bind(this);
  }

  componentDidMount() {
    this.props.getSurveyAction();
  }

  submit(e) {
    let answers = this.props.form.wizard.values;
    answers.pop();
    this.props.postSurveyAnswers(answers);

    this.props.history.push('/score');

  }

  nextQuestion(event) {
    this.setState({index: this.state.index + 1});
  }

  prevQuestion(event) {
    this.setState({index: this.state.index - 1});
  }

  renderQuestions() {
    if(!this.props.questions) {
      return null;
    }

    return this.props.questions.map((question, index) => {
      const answers = this.props.answers.filter((answer) => {
        return  answer.id === question.id;
      });

      let next = this.nextQuestion;
      if (this.state.index === (this.props.questions.length - 1) ) {
        next = this.submit;
      }

      return (
        this.state.index === index &&
        <Question
          category={question.category}
          id={question.id}
          key={question.id}
          onNext={next}
          onPrev={this.prevQuestion}
          question={question.question}
          answers={answers}
          index={index}
          questions={this.props.questions}
        />
      )
    });
  }

  render() {
    return (
      <div className="Quiz">
          {this.renderQuestions()}
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    form: state.form,
    questions: state.survey[0],
    answers: state.survey[1]
  }
}

Quiz = connect(mapStateToProps, {getSurveyAction, postSurveyAnswers})(Quiz);

export default reduxForm({
  form: 'quiz'
})(Quiz);
