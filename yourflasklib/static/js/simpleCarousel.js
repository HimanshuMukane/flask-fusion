$(document).ready(function() {
    const $carouselInnerSlider = $('.content_inner_slider');
    const $dots = $('.dots');
    const $prevButton = $('.prev_button');
    const $nextButton = $('.next_button');
    const $slide = $('#slide');
    const IMAGE_SIZE = $carouselInnerSlider.width();
    const TOTAL_IMAGES = $carouselInnerSlider.find('img').length - 1;
    let counter = 0;
    const ACTIVE_CLASS_NAME = 'active';
    const TIMER = 1500;
    const TRANSITION = 'all .3s ease-out';
    let intervalID = 0;

    function moveSliderToIndex(index) {
      $carouselInnerSlider.css('transform', `translateX(-${IMAGE_SIZE * index}px)`);
    }

    function addClassToIndex(className, index) {
      $carouselInnerSlider.find('img').eq(index).addClass(className);
    }

    function removeClassToIndex(className, index) {
      $carouselInnerSlider.find('img').eq(index).removeClass(className);
    }

    function addBackGroundToCurrentIndex(index) {
      $dots.find('.dot').eq(index).css('background', '#000');
    }

    function removeBackGroundToCurrentIndex(index) {
      $dots.find('.dot').eq(index).css('background', 'transparent');
    }

    function setTransition(transition) {
      $carouselInnerSlider.css('transition', transition);
    }

    function handleNextImage() {
      handleRemove();
      counter = (counter === TOTAL_IMAGES) ? -1 : counter;
      counter += 1;
      handleAdding();
      moveSliderToIndex(counter);
    }

    function handlePrevImage() {
      handleRemove();
      counter = (counter === 0) ? TOTAL_IMAGES + 1 : counter;
      counter -= 1;
      handleAdding();
      moveSliderToIndex(counter);
    }

    function handleDotClick(event) {
      const value = parseInt($(event.target).val());
      if (!isNaN(value)) {
        handleRemove();
        counter = value;
        moveSliderToIndex(counter);
        handleAdding();
      }
    }

    function handleSlideChange() {
      const isChecked = $slide.prop('checked');
      if (isChecked) {
        intervalID = setInterval(handleNextImage, TIMER);
      } else {
        clearInterval(intervalID);
        intervalID = null;
      }
    }

    function handleRemove() {
      removeClassToIndex(ACTIVE_CLASS_NAME, counter);
      removeBackGroundToCurrentIndex(counter);
    }

    function handleAdding() {
      addClassToIndex(ACTIVE_CLASS_NAME, counter);
      addBackGroundToCurrentIndex(counter);
    }

    $nextButton.on('click', handleNextImage);
    $prevButton.on('click', handlePrevImage);
    $dots.on('click', '.dot', handleDotClick);
    $slide.on('change', handleSlideChange);

    $carouselInnerSlider.on('transitionstart', function() {
      $nextButton.off('click', handleNextImage);
      $prevButton.off('click', handlePrevImage);
      $dots.off('click', handleDotClick);
      $slide.off('change', handleSlideChange);
    });

    $carouselInnerSlider.on('transitionend', function() {
      $nextButton.on('click', handleNextImage);
      $prevButton.on('click', handlePrevImage);
      $dots.on('click', '.dot', handleDotClick);
      $slide.on('change', handleSlideChange);
    });

    setTransition(TRANSITION);

    handleSlideChange();
  });