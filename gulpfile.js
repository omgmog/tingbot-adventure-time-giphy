var gulp = require('gulp');
var fs = require('fs');
var mkdirp = require('mkdirp');

var packageData = JSON.parse(fs.readFileSync('./src/app.tbinfo'));

gulp.task('default', function () {
  var dest = packageData.name + ' - v' + packageData.version + '.tingapp';

  mkdirp(dest);
  return gulp.src('./src/*.*')
  .pipe(gulp.dest(dest));
});