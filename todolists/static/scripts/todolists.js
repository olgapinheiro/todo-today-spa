// Add a "line-through" an item when it's clicked
function check_task(clicked_id){
    //var task_div = document.getElementById(clicked_id);
    var task_elmts = Array.from(document.getElementsByName(clicked_id));
    console.log(task_elmts);
    for(var e in task_elmts){
        console.log(task_elmts[e]);
        task_elmts[e].classList.toggle('checked');
    }
    //task_div.classList.toggle('checked');
}