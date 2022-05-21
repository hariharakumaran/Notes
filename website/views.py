from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Note
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteId']
    data = Note.query.get(note_id)
    if data:
        if data.user_id == current_user.id:
            db.session.delete(data)
            db.session.commit()

    return jsonify({})
