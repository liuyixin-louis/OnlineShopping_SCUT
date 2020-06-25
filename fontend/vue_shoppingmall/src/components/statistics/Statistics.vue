<template>
  <ve-line :data="chartData"></ve-line>
</template>

<script src="https://cdn.jsdelivr.net/npm/v-charts/lib/index.min.js"></script>

<script>
export default {
  data: function () {
    return {
      chartData: {
        columns: ['date', 'sale'],
        rows: []
      }
    }  },
  created () {
    this.getStatistics()
  },
  methods: {
    async getStatistics () {
      const { data: res } = await this.$http.get('admin/platform_statistics')
      console.log(res)
      this.chartData.rows = res.res

      console.log(this.chartData)
    }
  }

}
</script>