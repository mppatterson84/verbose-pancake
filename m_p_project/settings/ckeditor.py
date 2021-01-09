from .base import *

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BASE_PATH = "ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moonocolor',
        'removePlugins': ['image'],
        'extraPlugins': ['codesnippet', 'autogrow', 'image2', 'uploadwidget', 'uploadimage'],
        'codeSnippet_theme': 'docco',
        'autoGrow_onStartup': True,
        'autoGrow_minHeight': '300',
        'width': '100%',
        'image2_alignClasses': ['align-left', 'align-center', 'align-right'],
        'image2_prefillDimensions': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source'],
            ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent',
                'Indent', '-', 'Blockquote', 'CreateDiv'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight',
                'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
            ['Link', 'Unlink'],
            ['Image', '', 'Table',
                'HorizontalRule', 'Smiley', 'SpecialChar'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks'],
            ['CodeSnippet', 'UploadWidget', 'UploadImage'],
        ],
    }
}
