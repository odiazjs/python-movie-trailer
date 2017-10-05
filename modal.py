
class Modal():
    def __init__(self, options):
        self.options = options

    def open(self):
        modal_content = '''
        <div id="openModal" class="modalDialog">
            <div><a href="#close" title="Close" class="close">X</a>
                    <h2>Some Title</h2>
                <p>something here</p>
                <p>another something here</p>
            </div>
        </div>'''
        return modal_content