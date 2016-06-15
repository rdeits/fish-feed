require 'rake/clean'

directory "build/audio"
mkdir_p("build/audio")

Dir.chdir("build/audio") do
    sh "youtube-dl --format=bestaudio --output=\"%(upload_date)s/%(title)s.%(ext)s\" --write-info-json --restrict-filenames  \"https://www.youtube.com/playlist?list=PLSCKxbYNjB1qfYbOMVqTplCFeX18eqLlZ\""
end

webm_files = FileList['build/audio/**/*.webm']

mp3_files = webm_files.ext(".mp3")

rule ".mp3" => ".webm" do |t|
    sh "ffmpeg -i \"#{t.source}\" -acodec libmp3lame -aq 4 \"#{t.source.gsub(/\.webm/, '.mp3')}\""
end

multitask "build/rss.xml" => mp3_files do
    sh "python3 generate_feed.py"
end


task :default => "build/rss.xml" do
end

task :serve => :default do
    Dir.chdir("build") do
        sh "python3 -m http.server"
    end
end

CLEAN.include('build/audio/*.*', 'build/audio/*', 'build/*.xml')
CLOBBER.include('build')
