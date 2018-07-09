import React from "react"

import Title from "../components/Title"
import Authentication from "../components/Authentication"

export default class PageHeader extends React.Component {
    render() {
        return (
            <div className="PageHeader">
                <p>PageHeader</p>
                <Title />
                <Authentication />
            </div>
        )
    }
}