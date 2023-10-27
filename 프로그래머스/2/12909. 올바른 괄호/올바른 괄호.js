    //f t f f
    //( ) ) (
    //0 1 2 3

    //f f t t f t
    //( ( ) ) ( )
    //0 1 2 3 4 5

    //f f t f
    //) ( ) (
let check ={

}
function solution(s){
    var answer = false;
    var num = s.length
    let count = 0
    
    s = s.split("")
    
    for(let i =0 ;i<s.length; i++){
        if (count < 0){
            answer = false;
            break
        } 
        
        if(s[i] === "("){ count +=1 }
        else count -=1
        // console.log(count,s[i],i)
        
    }
    

    
    return count === 0 ? true :false ;
}