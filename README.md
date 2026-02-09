# A System for Tracking Players and the Ball in Association Football Matches using
Regular TV Footage in conjunction with “Deep Learning” and Transformational
Geometry


Sophisticated software for analysis of player performance and team tactics during sports matches is now
commonplace on TV Sports coverage, for “pundits” to give in-depth analysis to fans during breaks in, or at
the end of, the game. Such software is also used by coaches and managers of top clubs to work out what
went right and what went wrong in the match, and they can also analyse footage from other teams’ matches
to help develop strategies and tactics for use when their team plays one of those others. However, such
software often relies on footage from multiple camera views, using very high frame rate cameras. Hawk-Eye*
is one such system, and has been used with great success in TV coverage of sports such as cricket and tennis
for over 20 years, but relies on triangulation from multiple camera views from expensive cameras and a lot
of high performance computing.
In this paper, wedescribeourdevelopmentandevaluationofasystemfortrackingplayers,matchofficialsand
the ball in “regular” frame rate TV footage of Association Football (Soccer) matches. The system distinguishes
between players of the different teams, the match officials, and the ball, and is able to track all of these
with very good reliability. Our system is based on the latest version of the “You Only Look Once” (YOLOv11)
object detection algorithm, developed from the GoogleNet Convolutional Neural Network Architecture.
The system is fine-tuned and trained on a dedicated dataset tailored to optimize detection performance
in football-specific scenarios. Moreover, through implementing various transformational geometry and
Newtonian dynamics calculations, we are also able to compensate for motion of the camera, and produce
data and statistics for each player, such as their current speed of movement, and the total distance they
have travelled during the game.
Although our system may not be a sophisticated as the “state of the art” ones used by major sports TV
broadcasting companies, it has performed well when tested out on “regular” TV footage of professional
Association Football matches. This could make it feasible for use by lower level and semi-professional clubs,
or even fans’ channels, relying on less advanced technology


