import React from "react"

import Headline from "../components/Headline"
import PageHeader from "../containers/PageHeader"
import Lists from "../containers/Lists"
import Reports from "../containers/Reports"
import Footer from "../containers/Footer"

export default class App1Container extends React.Component {
    render() {
        return (
            <div className="allContainers">
            <div className="container">
              <div className="row">
                <div className="col-sm-12">
                  <Headline>Sample App! Testing! lalala</Headline>
                </div>
              </div>
            </div>
                <div className="PageHeader" ><PageHeader /></div>
                <div className="Lists" ><Lists /></div>
                <div className="Reports" ><Reports /></div>
                <div className="Footer"><Footer /></div>
            </div>
        )
    }
}