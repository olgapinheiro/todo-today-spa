import React from "react"

export default class Task extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        return (
            <div className="Task">
                <p>Task {this.props.type}</p>
            </div>
        )
    }
}