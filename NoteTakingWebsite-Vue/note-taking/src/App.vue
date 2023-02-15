<template>
  <div >
      <main>
        <div v-if="showModal" class="overlay">
          <div class="modal">
              <textarea name="note" id="note" cols="30" rows="10"></textarea>
              <button>Add Note</button>
              <button @click="showModal=false" class="close">Close</button>
          </div>
        </div>
        <div class="container">
          <header>
            <h1>Notes {{showModal}}</h1>
            <button @click="showModal=true">+</button>
          </header>
          <div class="cards-container">
            <div class="card">
              <p class="main-text">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sequi amet impedit, velit molestias fugit nisi!</p>
              <p class="date">03/03/2023</p>
            </div>
            <div class="card">
              <p class="main-text">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sequi amet impedit, velit molestias fugit nisi!</p>
              <p class="date">03/03/2023</p>
            </div>
          </div>

        </div>
      </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const showModal=ref(false);



</script>

<style scoped>
main{
  height: 100vh;
  width:100vw;
}
.container{
  max-width: 1000px;
  padding: 10px;
  margin: 0 auto;
}
header{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
h1{
  font-weight: bold;
  margin-bottom:25px ;
  font-size: 75px;
}
header  button{
  border:none;
  padding:10px;
  width: 50px;
  height: 50px;
  cursor:pointer;
  background-color: rgb(21, 20, 20);
  border-radius: 100%;
  color:white;
  font-size: 20px;
}
.card{
  width: 225px;
  height: 225px;
  background-color: rgb(237,182,44);
  padding:10px;
  border-radius: 15px;
  display: flex;
  flex-direction: column;
  justify-content:space-between;
  margin-right:20px;
  margin-bottom: 20px;
}
.date{
  font-size: 12.5px;
  font-weight: 100%;
}
.cards-container{
  display: flex;
  flex-wrap: wrap;
}
.overlay{
  position: absolute;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0,0,0,0.77);
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;

}
.modal{
  width: 750px;
  background-color: white;
  border-radius: 10px;
  padding: 30px;
  position: relative;
  display: flex;
  flex-direction: column;

}
.modal button{
  padding: 10px 20px;
  font-size: 20px;
  width: 100%;
  background-color:blueviolet;
  border:none;
  color:white;
  cursor:pointer;
  margin-top:15px;

}
.modal .close{
  background-color: rgb(193, 15, 15);
  margin-top: 7px;
}

</style>
