
function objectOperation(obj,operation,prop,new_value){
    if(operation == 'delete'){
        if(obj.hasOwnProperty(prop)){
            delete obj[prop]
            return obj
        }else{
            return obj
        }

    }

    if (operation == 'edit'){
        if(obj.hasOwnProperty(prop)){
            obj[prop] =  new_value
            return obj
        }else{
            return obj
        }
    }

}
obj = {
    'name' : 'mahbub',
    'age' : 26,
    'profession' : 'software engineer'
}
// results  = objectOperation(obj,'delete','name')
results  = objectOperation(obj,'edit','name')
console.log("results-->", results);
