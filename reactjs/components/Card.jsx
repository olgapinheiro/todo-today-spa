import React from "react"

import Task from "../components/Task"
import NewTask from "../components/NewTask"

export default class Card extends React.Component {
    constructor(props){
        super(props);
    }

    render() {
        const isList = this.props.type;
        const hasNewTask = this.props.type == "list" ? <NewTask /> : false ;

        return (
            <div className="Card">
                <p>Card</p>
                <Task type={this.props.type}/>
                {hasNewTask}
            </div>
        )
    }
}