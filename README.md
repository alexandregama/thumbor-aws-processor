# JSON Format to send a new message

```json
{
  "s3-url": "https://s3.amazonaws.com/procurando-thumbor-images/images/love-exclusivo.jpg",
  "original-image-name": "love-exclusivo-original.jpg",
  "bucket-name-original": "procurando-thumbor-images",
  "resize": [
      {"width": "200", "height": "200", "bucket-name": "procurando-thumbor-images", "image-name": "love-exclusivo-200x200.jpg"},
      {"width": "400", "height": "400", "bucket-name": "procurando-thumbor-images", "image-name": "love-exclusivo-400x400.jpg"},
      {"width": "600", "height": "600", "bucket-name": "procurando-thumbor-images", "image-name": "love-exclusivo-600x600.jpg"}
  ]
}
```

Installed Python dependencies

Pillow
```bash
$ pip3.5 install pillow
```

Requests
```bash
$ pip3.5 install requests
```
