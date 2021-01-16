from .base import *
from .static import *

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_BASE_PATH = "ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
    'default': {
        'contentsCss': [
            os.path.join(STATIC_URL, 'css/base.css'),
            'https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css'
        ],
        'skin': 'moonocolor',
        'removePlugins': ['image'],
        'extraPlugins': ['codesnippet', 'autogrow', 'image2'],
        'codeSnippet_theme': 'docco',
        'autoGrow_onStartup': True,
        'autoGrow_minHeight': '300',
        'width': '100%',
        'image2_prefillDimensions': False,
        'filebrowserBrowseUrl': '/browser/',
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
            ['CodeSnippet'],
        ],
    }
}
