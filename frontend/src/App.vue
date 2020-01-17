<template>
  <div>
    <button @click="search()">カードを探す</button>
    <div v-for="card in cards" v-bind:key="card.img">
      <p>{{ card["name"] }}</p>
      <p>{{ card["price"] }}</p>
      <p><img :src="card.img"/></p>
    </div>
  </div>
</template>

<style>
  img {
    width: 100px;
  }
</style>
<script>
export default {
  data () {
    return {
      cards: [],
      name: '',
      price: '',
    }
  },
  methods: {
    search () {
      fetch('/api')
      .then( response => {
        return response.json()
      })
      .then( response => {
        this.cards.push(response)
        for (let i = 0; i < response.length; i++) {
          let card = {
            "name": response[i]['name'],
            "price": response[i]['price'],
            "url": response[i]['url'],
            "img": response[i]['img']
          };
          this.cards.push(card)
        }
      })
      .catch( (err) => {
        this.msg = err // エラー処理
      });
    }
  }
}
</script>