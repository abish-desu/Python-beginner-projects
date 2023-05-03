import ytdl from "ytdl-core";     //kunjan way to download youtube videos
import { createWriteStream } from "fs";
import YouTube from "youtube-sr"

YouTube.searchOne("running up that hill")
    .then((video) => {
        console.log(video);
        // console.log(`Downloading ${video.title} by ${video.channel.name}`);
        // ytdl(video.url).pipe(createWriteStream(`./${video.title}.mp4`))
    })
