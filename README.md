# README #
#Written by Ricardo Williams II#
The Humboldt Project outlines a system that can be leveraged to combat phishing campaigns via an
aggressive counter measure. Most anti-phishing methods rely on a reactive approach. Humboldt on the
other hand will utilize people to submit fake credentials to phishing sites. In an effort to halt ambitious
phishing campaigns against an institution by flooding the phisher’s data with indistinguishable fake
credentials. For more information on the background on which this paper is being written, please refer to
the papers ”Crowd-sourced Phishing Disruption with Humboldt” and ”Leveraging the Crowds to Disrupt
Phishing”. This system’s goal is to create an environment in which data can be collected about an
institution, and effectively respond to active phishing campaigns against them. It will do so by accepting
configurations that will determine the structure of how usernames are formed in their organization (e.g.
the University of Oregon typically assigns usernames with a person’s first name appended by the first
letter of their last initial) as well as the requirements for their passwords. This information will be used to
generate fake, yet realistic looking credentials to flood the phishing sites. This system will use the
following structure and set of programs to achieve parts of that goal. A full fledged system will require a
more thorough set of scripts and fail safes. This serves as a starting template.
