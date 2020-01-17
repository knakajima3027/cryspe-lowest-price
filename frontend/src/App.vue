<template>
  <div>
    <input type="text" v-model="name">
    <input type="text" v-model="price">
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
      const params = { card_name: this.name, card_price: this.price};
      if (this.price === "") {
        params["card_price"] = 10 ** 20
      } 
      const qs = new URLSearchParams(params);
      fetch(`/api?${qs}`)
      .then( response => {
        return response.json()
      })
      .then( response => {
        this.cards = [];
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