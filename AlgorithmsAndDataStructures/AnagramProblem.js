function validagram(Anagram,Anagram2){
    if(Anagram.length !== Anagram2.length) {return false}
   
    AnagramArray=Anagram.split("");
    AnagramArray2=Anagram2.split("");
    for(i=0;i<Anagram.length;i++){
        
        let char =Anagram[i];
       
        let correctIndex=AnagramArray.indexOf(AnagramArray2[i])
        if(correctIndex===-1){ 
            return false
        };
       
    AnagramArray.splice(correctIndex,1)
       

    }
    return true

}