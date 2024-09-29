import React from "react";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {apiResponse: ""};
  }
  callAPI() {
    fetch("/show-data")
      .then(res => res.json())
      .then(res => this.setState({ apiResponse: res }));
  }
  componentDidMount() {
    this.callAPI();
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <p>{this.state.apiResponse}</p>
        </header>
      </div>
    );
  }
}
export default App;