import React from "react"

import Card from "../components/Card"

export default class NextPriorities extends React.Component {
    render() {
        return (
            <div className="NextPriorities">
                <p>NextPriorities</p>
                <Card type="next" />
            </div>
        )
    }
}