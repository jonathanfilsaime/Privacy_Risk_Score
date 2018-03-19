import React, {Component} from 'react';

import './styles.css';

class Recommendations extends Component {
  render() {
    console.log(this.props.rec)
    return (
      <div>
        <h3 className="Recommendations-recommendations">Recommendations</h3>
        {
          this.props.rec.map((rec) => {
            return (
              <div>
                <div className="Recommendations-video" dangerouslySetInnerHTML={{__html: rec.link}}>
                </div>
              </div>
            )
          })
        }
      </div>
    );
  }
}

export default Recommendations;

/*
<div className="Recommendations-category">
  {rec.category}
</div>
*/
