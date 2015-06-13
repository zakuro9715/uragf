var gulp = require('gulp');
var lessc = require('gulp-less');
var plumber = require('gulp-plumber');
var path = require('path');
var glob = require('glob');

var paths = {
  styles: 'styles',
  css:  'styles/**/*.css',
  less: 'styles/**/*.less',
  dist: 'static',
};


gulp.task('less', function() {
  options = {
    paths: paths.styles,
  }
  gulp.src(paths.less)
    .pipe(lessc(options))
    .pipe(gulp.dest(path.join(paths.dist, paths.styles)));
});

gulp.task('css', function() {
  gulp.src(paths.css)
    .pipe(gulp.dest(path.join(paths.dist, paths.styles)));
});

gulp.task('styles', ['css', 'less']);
