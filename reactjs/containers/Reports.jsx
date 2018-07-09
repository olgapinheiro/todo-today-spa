import React from "react"

import CompletedTasks from "../components/CompletedTasks"
import NextPriorities from "../components/NextPriorities"

export default class Reports extends React.Component {
    render() {
        return (
            <div className="Reports">
                <p>Reports</p>
                <CompletedTasks />
                <NextPriorities />
            </div>
        )
    }
}