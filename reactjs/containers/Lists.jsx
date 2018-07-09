import React from "react"

import Card from "../components/Card"

export default class Lists extends React.Component {
    render() {
        return (
            <div className="Footer">
                <p>Lists</p>
                <Card type="lists" />
            </div>
        )
    }
}