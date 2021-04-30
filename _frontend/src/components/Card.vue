<template>
  <md-card>
    <md-card-media-cover md-solid>
      <md-card-media md-ratio="16:9">
        <router-link :to="'/post/' + id" ><img :src="image"></router-link>
      </md-card-media>

      <md-card-area>
        <md-card-header>
         <span class="md-title">{{TrimTitle(title)}}</span>
        </md-card-header>
      </md-card-area>
    </md-card-media-cover>
  </md-card> 
</template>

<script>
export default {
    name: 'Card',
    props: {
      image: String,
      title: String,
      id: Number
    },
    methods: {
      TrimTitle(title) {
        const MaxLength = 27;
        if(title.length <= MaxLength) { return title; }
        else {
          for(let i = MaxLength; i > 0; i--) {
            if(title[i] === ' ') {
              title = title.slice(0,i);
              title += "...";
              break; }
          }
          return title }  
      }
    },
    data() {
        return { }
    },
}
</script>

<style scoped>
.md-card {
    width: 100%;
    margin: 8px;
    display: inline-block;
    vertical-align: top;
}
.md-card .md-title {
  font-size:22px;
  letter-spacing: 0;
  line-height: 32px;
}

</style>
