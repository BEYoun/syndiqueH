

/************************************************
*               Remove Thumbnail                *
************************************************/
Dropzone.options.dpzRemoveThumb = {
  paramName: "file", // The name that will be used to transfer the file
  maxFilesize: 1, // MB
  addRemoveLinks: true,
  dictRemoveFile: " Trash",
  init: function () {

    // Using a closure.
    var _this = this;

    // Setup the observer for the button.
    $("#dpz-remove-thumb").on("sending", function(file, xhr, formData) {
      // Will send the filesize along with the file as POST data.
      formData.append("filesize", file.size);
    });
  }
}

/*****************************************************
*               Remove All Thumbnails                *
*****************************************************/
Dropzone.options.dpzRemoveAllThumb = {
  paramName: "file", // The name that will be used to transfer the file
  maxFilesize: 1, // MB
  init: function () {

    // Using a closure.
    var _this = this;

    // Setup the observer for the button.
    $("#clear-dropzone").on("click", function () {
      // Using "_this" here, because "this" doesn't point to the dropzone anymore
      _this.removeAllFiles();
      // If you want to cancel uploads as well, you
      // could also call _this.removeAllFiles(true);
    });
  }
}
