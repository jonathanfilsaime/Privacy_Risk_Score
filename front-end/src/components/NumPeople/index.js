import React, {Component} from 'react';
import { color } from 'd3-color';
import { interpolateRgb } from 'd3-interpolate';
import LiquidFillGauge from 'react-liquid-gauge';

import './styles.css';

class NumPeople extends Component {
  state = {
      value: 50
  };
  startColor = '##00e64d';
  endColor = '#00ff55';

  render() {
    let {data} = this.props;
    if(typeof(data) === 'string') {
      data = data.slice(0, -1)
    } else {
      return (
        <div className="card NumPeople">
          <h1 className="NumPeople-header">{this.props.data}</h1>
          <div className="NumPeople-caption">{this.props.caption}</div>
        </div>
      )
    }

    const radius = 135;
    const interpolate = interpolateRgb(this.startColor, this.endColor);
    const fillColor = interpolate(data / 100);
    const gradientStops = [
        {
            key: '0%',
            stopColor: '#ff3300',
            stopOpacity: 1,
            offset: '0%'
        },
        {
            key: '25%',
            stopColor: '#ff9900',
            stopOpacity: 1,
            offset: '0%'
        },
        {
            key: '50%',
            stopColor: '##ffff00',
            stopOpacity: 0.75,
            offset: '50%'
        },
        {
            key: '100%',
            stopColor: '#33cc33',
            stopOpacity: 0.5,
            offset: '100%'
        }
    ];

    return (
      <div className="card NumPeople">
        <div className="NumPeople-liquid">
        <LiquidFillGauge
            style={{ margin: '0 auto' }}
            width={radius * 2}
            height={radius * 2}
            value={data}
            percent="%"
            textSize={1}
            textOffsetX={0}
            textOffsetY={0}
            textRenderer={(props) => {
                const value = Math.round(data);
                const radius = Math.min(props.height / 2, props.width / 2);
                const textPixels = (props.textSize * radius / 2);
                const valueStyle = {
                    fontSize: textPixels
                };
                const percentStyle = {
                    fontSize: textPixels * 0.6
                };

                return (
                    <tspan>
                        <tspan className="value" style={valueStyle}>{value}</tspan>
                        <tspan style={percentStyle}>{'%'}</tspan>
                    </tspan>
                );
            }}
            riseAnimation
            waveAnimation
            waveFrequency={2}
            waveAmplitude={1}
            gradient
            gradientStops={gradientStops}
            circleStyle={{
                fill: 'black'
            }}
            waveStyle={{
                fill: fillColor
            }}
            textStyle={{
                fill: color('#444').toString(),
                fontFamily: 'Arial'
            }}
            waveTextStyle={{
                fill: color('#fff').toString(),
                fontFamily: 'Arial'
            }}
            onClick={() => {
                this.setState({ value: Math.random() * 100 });
            }}
        />
        </div>
        <div className="NumPeople-caption">{this.props.caption}</div>
      </div>
    );
  }
}

export default NumPeople;
