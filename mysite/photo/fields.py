import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile


class ThumbnailImageFieldFile(ImageFieldFile):  # 파일 시스템에 직접 파일을 쓰고 지우는 작업을 함
    def _add_thumb(s):  # 이 메소드는 기존 이미지 파일명을 기준으로 썸네일 이미지 파일명을 만들어줌
        parts = s.split(".")
        parts.insert(-1, "thumb")
        # 이미지 확장자가 jpeg or jpg가 아니면 jpg로 변경합니다.
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return ".".join(parts)

    @property
    def thumb_path(self):
        return self._add_thumb(self.path)
     # 이미지를처리하는 필드는 파일의 경로와 URL 속성을 제공해야한다
     # 이 메소드는 원본파일의 경로인 path 속성에 추가해 썸네일의 경로인 Thumb_path 속성을 만든다
     # @property 데코레이터를 이용해 메소드를 멤버 변수처럼 사용할 수 있음

    @property
    def thumb_url(self):
        return self._add_thumb(self.url)
     # 이 메소드는 원본파일의 URL인 url 속성에 추가해 썸네일의 URL인 thunb_url 속성을 만든다

    def save(self, name, content, save=True):  # 파일 시스템에 파일을 저장하고 생성하는 메소드
        super().save(name, content, save)

        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int(size[0] - img.size[0])/2), int((size[1] - img.size[1]/2))
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)
