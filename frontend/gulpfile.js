var gulp = require('gulp');
var lessc = require('gulp-less');
var plumber = require('gulp-plumber');
var path = require('path');
var glob = require('glob');

var searchApps = function(root) {
  root = root || __dirname;
  return glob.sync(path.join(root, '/**/__init__.py')).map(function(v) {
    return path.dirname(v);
  });
};

var paths = {
  styles: 'styles',
  less: 'styles/**/*.less',
  dist: 'static',
};


gulp.task('less', function() {
  apps = searchApps();
  options = {
    paths: apps.map(function(v) { return path.join(v, paths.styles) }),
  }
  apps.forEach(function(app) {
    gulp.src(path.join(app, paths.less))
      .pipe(lessc(options))
      .pipe(gulp.dest(path.join(app, paths.dist, paths.styles)));
  });
});
