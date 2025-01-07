<template>
  <div id="app">
    <table class="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>SecID</th>
          <th>Короткое название</th>
          <th>Рег. номер</th>
          <th>Название</th>
          <th>ISIN</th>
          <th>Торгуется</th>
          <th>ID эмитента</th>
          <th>Название эмитента</th>
          <th>ИНН эмитента</th>
          <th>ОКПО эмитента</th>
          <th>Гос. регистрация</th>
          <th>Тип</th>
          <th>Группа</th>
          <th>Основная площадка</th>
          <th>Площадка рыночной цены</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in data" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.secid }}</td>
          <td>{{ item.shortname }}</td>
          <td>{{ item.regnumber }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.isin }}</td>
          <td>{{ item.is_traded }}</td>
          <td>{{ item.emitent_id }}</td>
          <td>{{ item.emitent_title }}</td>
          <td>{{ item.emitent_inn }}</td>
          <td>{{ item.emitent_okpo }}</td>
          <td>{{ item.gosreg }}</td>
          <td>{{ item.type }}</td>
          <td>{{ item.group }}</td>
          <td>{{ item.primary_boardid }}</td>
          <td>{{ item.marketprice_boardid }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      data: [], // Данные для таблицы
    };
  },
  async created() {
    try {
      // Получаем данные с бэкенда
      const response = 'aaa'//await axios.get('http://localhost:3000/api/data');
      this.data = response.data;
    } catch (error) {
      console.error('Ошибка при получении данных:', error);
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}

.table {
  width: 100%;
  margin: 0 auto;
  border-collapse: collapse;
}

.table th, .table td {
  padding: 12px;
  border: 1px solid #ddd;
}

.table th {
  background-color: #f8f9fa;
  font-weight: bold;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}

.table-striped tbody tr:hover {
  background-color: #f1f1f1;
}
</style>