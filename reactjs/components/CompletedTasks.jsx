import React from "react"

import Card from "../components/Card"

export default class CompletedTasks extends React.Component {
    render() {
        return (
            <div className="CompletedTasks">
                <p>CompletedTasks</p>
                <Card type="completed" />
            </div>
        )
    }
}