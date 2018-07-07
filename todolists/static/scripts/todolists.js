// Add a "line-through" an item when it's clicked
function check_task(clicked_id){
    //var task_div = document.getElementById(clicked_id);
    var task_elmts = Array.from(document.getElementsByName(clicked_id));
    console.log(task_elmts);
    task_id=clicked_id.split('-');
    for(var e in task_elmts){
        console.log(task_elmts[e]);
        task_elmts[e].classList.toggle('checked');
        view_url = 'http://localhost:8000/todolists/'+task_id[1]+'/complete_task';
        console.log(view_url);
        //window.location.href = view_url;
    }
}