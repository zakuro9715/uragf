var path = require("path");

module.exports = {
  entry: {
    app: [
      './scripts/app.js',
      './scripts/rooms/room.js',
      './scripts/rooms/room_list.js',
    ],
  },
  output: {
    path: path.join(__dirname, 'static'),
    filename: '[name].js',
  }
}
